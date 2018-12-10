// page/component/new-pages/cart/cart.js
const app = getApp()

Page({
  data: {
    carts: [],               // 购物车列表
    hasList: true,          // 列表是否有数据
    totalPrice: 0,           // 总价，初始为0
    selectAllStatus: false,    // 全选状态，默认全选
  },

  
  onLoad(e) {


  },

  onShow() {
    this.setData({
      hasList: true
    });
    wx.showLoading({
      title: '加载中',
    })
    this.getlove()
  },


  onHide: function () {
  },


  /**
   * 删除收藏的当前商品
   */
  deleteList(e) {
    wx.showLoading({
      title: '加载中',
    })
    const index = e.currentTarget.dataset.index;
   
    let carts = this.data.carts;
    app.getInfoWhere('love', { id: e.currentTarget.dataset._id},e3=>{

      app.deleteInfoFromSet('love', e3.data[0]['_id'],e4=>{
 
        wx.showToast({
          title: '删除成功',
        })
        carts.splice(index, 1);
        this.setData({
          carts: carts
        });

        if (!carts.length) {
          this.setData({
            hasList: false
          });
        } else {

        }
      })
      })
      
   
  },


  getlove (e){
    app.getInfoWhere('love', {}, res => {
     //console.log(res.data)
     const id_list = []
      for (let i = 0; i < res.data.length; i++) {
        id_list.push(res.data[i]['id'])
      }
      //console.log(id_list)
      const db = wx.cloud.database()
      const _ = db.command
   
      app.getInfoWhere('fruit-board', { _id: _.in(id_list)}, e => {

        console.log(e)
        this.setData({
          carts: e.data
        });
        let carts = this.data.carts
        wx.hideLoading() 
        if (carts.length == 0) {
          this.setData({
            hasList: false
          });
        } else {
          this.setData({
            hasList: true,

          });
          
        }

      })

       
    })
 
 
   
  }





})