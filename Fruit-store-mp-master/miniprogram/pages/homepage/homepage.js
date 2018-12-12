// miniprogram/pages/homepage/homepage.js


const app = getApp()

Page({
  
  data: {
    swiperImgNo: 1,
    imgSwiperUrl: '',
    fruitInfo: [],
    goodsinfo:{},
    curPage: 1,
    pageSize: 10,
    loadingMoreHidden: true,
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
      title: '加载中',
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
 
    console.log(this.data.goodsinfo)
    this.setData({
      activeTypeId: parseInt(e.currentTarget.id),
      loadingMoreHidden:true,
      curPage:1,
      fruitInfo: []
    });
    this.onswitch()
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
      title: '加载中',
    })
     
    that.setData({
      isShow: true
    })
    // 获取openId
    this.getOpenid();
  },

  onReady: function () {
    //console.log(getCurrentPages()["0"].data)
    
  },


  onShow: function () {
    this.onswitch()
   
  },
  onswitch:function(){
    let now = this.data.goodsinfo
    let id = this.data.activeTypeId.toString()
    //如果已经加载过数据直接赋值
    if (now.hasOwnProperty(id)) {
      console.log(now[id])
      this.setData({
        fruitInfo: now[id].goods
      });
      //如果不存在进行数据加载
    } else {
      this.data.goodsinfo[this.data.activeTypeId.toString()] = { curPage: 1, goods: [] }
      if (id == '0') {
        this.getdata({})
      } else {
        this.getdata({ myClass: id })
      }
    }
  },

  onHide: function () {

  },

  onUnload: function () {

  },
  getdata: function (filter){
    console.log(filter)
    wx.showLoading({
      title: '加载中',
    })
    
    console.log(this.data.goodsinfo)
    let id = this.data.activeTypeId.toString()
    wx.cloud.callFunction({
      name: 'pageination',
      data: {
        dbName: 'fruit-board',
        filter: filter,
        pageIndex: this.data.goodsinfo[id].curPage,
        pageSize: this.data.pageSize,
      }
    }).then(res => {
      //console.log(res.result.haseMore)

      // if (!res.result.haseMore){
      //   this.setData({
      //     loadingMoreHidden: false
      //   });
      // }
      
      this.data.goodsinfo
      let goods = [...this.data.goodsinfo[id].goods, ...res.result.data]
      
      console.log(goods)
      let page = this.data.goodsinfo[id].curPage
      let info = this.data.goodsinfo
      info[id] = {curPage:page,goods:goods,loadingMoreHidden:res.result.haseMore}
      console.log(page)
      this.setData({
        fruitInfo:goods,
        goodsinfo:info,
        isShow: true
      })
      wx.hideLoading()
    })
  },
  onPullDownRefresh: function () {
    this.setData({
      curPage: 1
    });
    this.getdata({})
  
  },

  onReachBottom: function () {
    let info = this.data.goodsinfo
    if (info[this.data.activeTypeId.toString()].loadingMoreHidden){
      info[this.data.activeTypeId.toString()].curPage = info[this.data.activeTypeId.toString()].curPage+1;
      this.getdata({});
      this.setData({
          goodsinfo: info
      });
   
    }else{
      wx.showToast({
        title: '没有更多啦',
        icon: '',
        image: '',
        duration: 500,
        mask: true,
        success: function(res) {},
        fail: function(res) {},
        complete: function(res) {},
      })
    }

  },

  onShareAppMessage: function () {
    return {
      title: 'AO奥品汇',
      imageUrl: '../../images/icon/fruit.jpg',
      path: '/pages/homepage/homepage'
    }
  }

})