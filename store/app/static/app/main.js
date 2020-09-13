// Vue Instance

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

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
    },
    methods: {
        changeStatus(id) {
            axios.patch(`/api/profile/${id}/`, {
                completed: this.info.completed = !this.info.completed
            })
            .then(res => console.log(res))
            .catch(err => console.log(err))
        }
    },
    mounted() {
        axios
            .get('/api/profile')
            .then(response => (this.info = response.data))
    }
})