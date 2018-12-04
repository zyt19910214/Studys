// page/component/new-pages/cart/cart.js
const app = getApp()

Page({
  data: {
    carts: [],               // 购物车列表
    hasList: false,          // 列表是否有数据
    totalPrice: 0,           // 总价，初始为0
    selectAllStatus: false,    // 全选状态，默认全选
  },

  
  onLoad(e) {
   
  },

  onShow() {
    this.getlove()
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
    console.log(carts)
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
  },
  getlove (e){
    app.getInfoWhere('love', {}, res => {
     //console.log(res.data)
     const id_list = []
      for (let i = 0; i < res.data.length; i++) {
        id_list.push(res.data[i]['id'])
      }
      // console.log(id_list)
      const db = wx.cloud.database()
      const _ = db.command
   
      app.getInfoWhere('fruit-board', { _id: _.in(id_list)}, e => {
        //console.log(e)
        this.setData({
          carts: e.data
        });
        let carts = this.data.carts
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