// page/component/new-pages/cart/cart.js
const app = getApp()

Page({
  data: {
    carts: [],               // 购物车列表
    hasList: false,          // 列表是否有数据
    totalPrice: 0,           // 总价，初始为0
    selectAllStatus: false,    // 全选状态，默认全选
  },

  // 获取用户openid
  getOpenid() {
    let that = this;
    wx.cloud.callFunction({
      name: 'login',
      complete: res => {
        console.log('云函数获取到的openid:', res)
        var openid = res.result.openid;
        //console.log(openid) 
      }
    })
  },
  
  onLoad(e) {
    var that = this

    that.setData({
      isShow: true
    })
    // 获取openId
    this.getOpenid();
 
  },

  onShow() {
    let carts = this.data.carts;
    console.log('now openid:',this.data )
    app.getInfoWhere('love', { },
      e => {
        this.setData(
          {carts:e.data}
        )
        
      })
    if (carts.length == 0 ) {
      this.setData({
        hasList: false
      });
    } else {

      this.setData({
        hasList: true
      });
     
    }
  },

  onHide: function () {
    var self = this

    self.selectAll();
  },

  /**
   * 当前商品选中事件
   */
  selectList(e) {
    var self = this
    const index = e.currentTarget.dataset.index;
    let carts = this.data.carts;
    const selected = carts[index].selected;
    carts[index].selected = !selected;
    this.setData({
      carts: carts
    });
    app.globalData.carts = carts
  },

  /**
   * 删除购物车当前商品
   */
  deleteList(e) {
    const index = e.currentTarget.dataset.index;
    let carts = this.data.carts;
    carts.splice(index, 1);
    this.setData({
      carts: carts
    });
    app.globalData.carts = carts
    if (!carts.length) {
      this.setData({
        hasList: false
      });
    } else {
      
    }
  },

  /**
   * 购物车全选事件
   */
  selectAll(e) {
    let selectAllStatus = this.data.selectAllStatus;
    selectAllStatus = !selectAllStatus;
    let carts = this.data.carts;

    for (let i = 0; i < carts.length; i++) {
      carts[i].selected = selectAllStatus;
    }
    this.setData({
      selectAllStatus: selectAllStatus,
      carts: carts
    });
    app.globalData.carts = carts
  },





})