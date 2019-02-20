<template>
  <div id="app">
    <ReactiveBase
      app="real_last"
      url="https://lf4mFiiji:0addb6b7-4fc1-4e8b-add8-466ca2922758@scalr.api.appbase.io">
      <MultiList
        componentId="Sentsum"
        dataField="sentsum.keyword"
        title="Select Sentiment"
        selectAllLabel="All Sentiments"
        class="filter"
        :react="{ and: ['Emosum']}"/>
      <MultiList
        componentId="Emosum"
        dataField="emosum.keyword"
        title="Select Emotion"
        selectAllLabel="All Emotions"
        class="filter"
        :react="{ and: ['Sentsum']}"/>
    </ReactiveBase>
    <result-list
      componentId="SearchResult"
      dataField="review_data.keyword"
      :pagination="true"
      :from="0"
      :size="8"
      :showResultStats="true"
      className="result-list-container"
      :react="{ and: ['Sentsum', 'Emosum'] }"
     :renderData="reviewsList"/>
  </div>
</template>

<script>
  export default {
    name: "app",
    methods: {
      reviewsList(data) {
        return {
          title: data.review_data,
        };
      }
    }
  };

</script>

<style>
  #app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
