// Vue Instance
cartPage = new Vue({
    delimiters: ['[[', ']]'],
    el: '#cartPage',
    data: {
        message: 'Cart:',
        items: [],
    },
    methods: {

    },
    computed: {

    },
    mounted: function (){
        axios.get('/api/cart/')
            .then(response => {
            this.items = response.data
            })
    },
})