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

userProfile = new Vue({
    delimiters: ['[[', ']]'],
    el: '#userProfile',
    data: {
        message: 'Account',
        info: [],
        profiles: [
        {
            user: 'Alice',
            email: 'alice@store.com',
            address: '123 W Trindle Rd, Mechanicsburg PA 17055',
            preferred: false,
        },
        {
            user: 'Bob',
            email: 'bob@store.com',
            address: '456 Simpson St, Mechanicsburg PA 17055',
            preferred: false,
        },
        {
            user: 'Charlie',
            email: 'charlie@store.com',
            address: '555 Marble St, Mechanicsburg PA 17055',
            preferred: false,
        },
        ]

        
    },
    mounted() {
        axios
            .get('/api/profile')
            .then(response => (this.info = response.data))
    }
})