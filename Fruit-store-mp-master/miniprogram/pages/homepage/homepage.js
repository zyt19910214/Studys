// miniprogram/pages/homepage/homepage.js


const app = getApp()

Page({

  onPullDownRefresh() {
    wx.showToast({
      title: 'loading...',
      icon: 'loading'
    })
    //console.log('onPullDownRefresh', new Date())
  },
  
  data: {
    swiperImgNo: 1,
    imgSwiperUrl: '',
    fruitInfo: [],
    typeCat: [
      { id: 0, name: "全部商品" },
      { id: 1, name: "高档套盒" },
      { id: 2, name: "奶粉" },
      { id: 3, name: "儿童保健品" },
      { id: 4, name: "儿童洗护" },
      { id: 5, name: "奶瓶杯子" },
      { id: 6, name: "成人保健品" },
      { id: 7, name: "大牌彩妆" },
      { id: 8, name: "面膜" },
      { id: 9, name: "护肤品" },
      { id: 10, name: "红酒" },
      { id: 11, name: "生活用品" },
      { id: 12, name: "休闲娱乐" },
      
    ],
    activeTypeId:0,
    isShow:false,
    toView: "t0",
    openid: ''
  },
  onPageScroll(e) {
   
  },

  // 获取用户openid
  getOpenid() {
    let that = this;
    wx.cloud.callFunction({
      name: 'login',
      complete: res => {
        console.log('云函数login返回结果:', res)
        var openid = res.result.openid;
        console.log('云函数获取到的openid:', openid)
        //console.log(openid)
        that.setData({
          openid: openid
        })
      }
    })
  },

  // ------------加入收藏------------
  addLoveByHome: function(e) {
    wx.showLoading({
      title: 'loading',
    }) 
    //console.log(e.currentTarget.dataset)
    var self = this
    app.getInfoWhere('fruit-board', { _id: e.currentTarget.dataset._id },
      e => {
      //console.log(e.data["0"]._id)
 
       app.isNotRepeteToLove({ id: e.data["0"]._id,_openid:this.data.openid})
          
      }
    )
  },
 

  // ------------分类展示切换---------
  typeSwitch: function(e) {
   //console.log(e)
    getCurrentPages()["0"].setData({
      activeTypeId: parseInt(e.currentTarget.id)
    })
    switch (e.currentTarget.id) {
      // 全部展示
      case '0':
        app.getInfoFromSet('fruit-board', {},
          e => {
            // console.log(e.data)
            getCurrentPages()["0"].setData({
              fruitInfo: e.data
            })
          }
        )
        break;
      // 今日特惠
      case '1':
        app.getInfoWhere('fruit-board', {myClass:'1'},
          e => {
            getCurrentPages()["0"].setData({
              fruitInfo: e.data
            })
          }
        )
        break;
      // 销量排行
      case '2':
        app.getInfoByOrder('fruit-board','purchaseFreq','desc',
          e => {
            getCurrentPages()["0"].setData({
              fruitInfo: e.data
            })
          }
        )
        break;
      // 店主推荐
      case '3':
        app.getInfoWhere('fruit-board', { recommend: '1' },
          e => {
            getCurrentPages()["0"].setData({
              fruitInfo: e.data
            })
          }
        )
        break;
    }
  },
  tap() {
    let toView = this.data.toView
    for (let i = 0; i < this.data.typeCat.length; ++i) {
      console.log(this.data.toView)
      if ("t"+this.data.typeCat[i]['id'] == this.data.toView) {
        console.log('11111')
        this.setData({
          toView: "t"+this.data.typeCat[i + 3]['id'],
        })
        console.log(toView)
        break
      }
    }
    
  },

  // ---------点击跳转至详情页面-------------
  tapToDetail: function(e) {
    wx.navigateTo({
      url: '../detail/detail?_id=' + e.currentTarget.dataset.fid,
    })
  },


  // ------------生命周期函数------------
  onLoad: function (options) {
    var that = this
    wx.showLoading({
      title: 'loading',
    })
     
    that.setData({
      isShow: true
    })
    // 获取openId
    this.getOpenid();
  },

  onReady: function () {
    // console.log(getCurrentPages()["0"].data)
    
  },


  onShow: function () {
    var that = this
    // console.log(that.data)
    app.getInfoFromSet('fruit-board', {},
      e => {
        //console.log(e.data)
        getCurrentPages()["0"].setData({
          fruitInfo: e.data,
          isShow: true
        })
        wx.hideLoading()
      }
    )
  },

  onHide: function () {

  },

  onUnload: function () {

  },

  onPullDownRefresh: function () {

  },

  onReachBottom: function () {

  },

  onShareAppMessage: function () {
    return {
      title: 'AO奥品汇',
      imageUrl: '../../images/icon/fruit.jpg',
      path: '/pages/homepage/homepage'
    }
  }

})