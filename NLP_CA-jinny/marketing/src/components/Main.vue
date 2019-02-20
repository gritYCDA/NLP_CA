<template>
<div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <button v-on:click='getresults_sample("happy")'>getAll</button>
      <div class="card" v-for="review in results"> <!-- Loop through the results array, if pos is 1 (done) then we'll show it. -->
        <div class="card-content">
          <div class="content">
            {{ review.reviewtext }}
            {{ review.emosum }}
            {{ review.sentsum }}
            {{ review.keyword1 }}
          </div>
        </div>
      </div>
    </div>
  </div>

</template>




<script>
  import axios from 'axios'

  export default {
    name: 'Main',
    data() {
      return {
        results: [], // Array for holding the results
        reviewtext: '',
        sentsum: '',
        pos: 0,
        neut: 0,
        neg: 0,
        emosum: '',
        happy: 0,
        angry: 0,
        excited: 0,
        sad: 0,
        bored: 0,
        afraid: 0,
        disgust: 0,
        keyword1: '',
        keyword2: '',
        keyword3: '',
      }
    },
    mounted() { // This will be called when HelloWorld is loaded
      this.getallresults(); // Call our getresults function below
    },
    methods: {
      getallresults() {
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/review/',
          auth: {
            username: 'admin',
            password: 'admin123!'
          }
        }).then(response => this.results = response.data);
      },



      getresults_sample(result) {
        let reviews = [];

        for (let i = 0; i < this.results.length; i++) {
          if (this.results[i].sentsum === result) {
            reviews.append(this.results[i])
            continue
          }
          if (this.results[i].emosum === result) {
            reviews.append(this.results[i])
            continue
          }
        }

        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/review/',
          data: {
            results: reviews
          },
          auth: {
            username: 'admin',
            password: 'admin123!'
          }
        })
      },


    }
  }

</script>





<style scoped>
.select, select { /* 100% width for the select */
  width: 100%;
}

.card { /* Adding some air under the results */
  margin-bottom: 25px;
}

.done { /* Make the done results a little bit transparent */
  opacity: 0.3;
}
</style>