// page/component/new-pages/user/user.js
const app = getApp();

Page({
  data: {
    isAdmin: -1,
    openid: '',
    adiminArr: [
      '',
      'oenS94lGcw7qyDo0AZ7uWBqeo0Lg'
    ]
  },
  onLoad() {
    var that = this;
    that.getOpenid();
    // console.log(that.data)
  },

  onShow() {
  
  },

  // 获取用户openid
  getOpenid() {
    var that = this;
    wx.cloud.callFunction({
      name: 'login',
      complete: res => {
        console.log('云函数获取到的openid: ', res.result.openid)
        var openid = res.result.openid;
        var isAdmin = null;
        that.setData({
          openid: openid,
          isAdmin: that.data.adiminArr.indexOf(openid)
        })
      }
    })
  },

  goToBgInfo: function() {
    wx.navigateTo({
      url: '/pages/bgInfo/bgInfo',
    })
  }
})