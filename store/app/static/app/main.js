// Vue Instance
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

cartPage = new Vue({
    delimiters: ['[[', ']]'],
    el: '#cartPage',
    data: {
        message: 'Cart:',
        items: [],
        totals: "",
        profile: [],
        errorCount: "",

    },
    methods: {
        decreaseQuantity: function(id){
                const url = "/api/cart/" + id + "/";
                const item = this.items.filter(item => item.id === id)[0];
                axios.patch(url, {
                    quantity: item.quantity - 1
                })
                .then(response => {
                    this.items.forEach(item => {
                        if (item.id === response.data.id) {
                            item.quantity = response.data.quantity;
                            item.item_total = response.data.item_total;
                        }
                    })
                    axios.get('/api/totals/')
                        .then(response => {
                        this.totals = response.data
                        console.log(response)
                        })
                });
        },
        increaseQuantity: function(id){
                const url = "/api/cart/" + id + "/";
                const item = this.items.filter(item => item.id === id)[0];
                axios.patch(url, {
                    quantity: item.quantity + 1
                })
                .then(response => {
                    this.items.forEach(item => {
                        if (item.id === response.data.id) {
                            item.quantity = response.data.quantity;
                            item.item_total = response.data.item_total;
                        }
                    })
                    axios.get('/api/totals/')
                        .then(response => {
                        this.totals = response.data
                        console.log(response)
                        })
                });
        },
        deleteCartItem: function(id) {
              const url = "/api/cart/" + id + "/";
              axios.delete(url)
                  .then(response => {
                    axios.get('/api/cart/')
                        .then(response => {
                        this.items = response.data
                        });
                    axios.get('/api/totals/')
                        .then(response => {
                        this.totals = response.data
                        });
                  });
        },
        checkout: function() {
            pass
//            if (profile[0].preferred){
//                this.items.ForEach(item =>
//                    axios.post('/api/transactions/', {
//                        user: this.item.user
//                        product_name: this.item.product_name
//                        quantity_purchased: this.item.quantity
//                        transaction_total: this.item.discounted_item_total
//                        })
//                    axios.delete("/api/cart/" + this.item.id + "/")
//                    const products_url = "/api/products/" + this.item.product_name.id + "/";
//                    axios.patch(products_url, {
//                        inventory: this.item.product_name.inventory - this.item.quantity
//                    })
//                );
//            },
//            else {
//                this.items.ForEach(item =>
//                    axios.post('/api/transactions/', {
//                        user: this.item.user
//                        product_name: this.item.product_name
//                        quantity_purchased: this.item.quantity
//                        transaction_total: this.item.item_total
//                        })
//                    axios.delete("/api/cart/" + this.item.id + "/")
//                    const products_url = "/api/products/" + this.item.product_name.id + "/";
//                    axios.patch(products_url, {
//                        inventory: this.item.product_name.inventory - this.item.quantity
//                    })
//                );
//            }
        },
    },
    computed: {
        countCheckoutError: function () {
            this.errorCount = 0
            this.items.forEach(item => {
                if (item.quantity > item.product_name.inventory) {
                    this.errorCount++
                    console.log(this.errorCount)
                }
            })
        }
    },
    mounted:
        function (){
            axios.get('/api/cart/')
                .then(response => {
                this.items = response.data
                console.log(response)
                });
            axios.get('/api/totals/')
                .then(response => {
                this.totals = response.data
                console.log(response)
                });
            axios.get('/api/profile/')
                .then(response => {
                this.profile = response.data
                console.log(response)
                });
        },
})

userProfile = new Vue({
    delimiters: ['[[', ']]'],
    el: '#userProfile',
    data: {
        message: 'My Account',
        title: "Transaction History",
        info: [],
    },
    methods: {
        changeStatus(id) {
            axios.patch(`/api/profile/${id}/`, {
                preferred: this.info.preferred = !this.info.preferred
            })
            .then(res => console.log(res))
            .catch(err => console.log(err))
        }
    },
    mounted() {
        axios
            .get('/api/profile/')
            .then(response => (this.info = response.data))
    }
})

transactionHistory = new Vue({
    delimiters: ['[[', ']]'],
    el: '#transactionHistory',
    data: {
        title: "Transaction History",
        transactions: [],
    },
    mounted() {
        axios
            .get('/api/transactions/')
            .then(response => (this.transactions = response.data))
    }
})