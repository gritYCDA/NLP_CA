<template>
  <div id="app">
    <ReactiveBase
      app="real_last"
      url="https://lf4mFiiji:0addb6b7-4fc1-4e8b-add8-466ca2922758@scalr.api.appbase.io">
      <div class="left-bar">
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
      </div>
      <result-list
      componentId="SearchResult"
      dataField="review_data.keyword"
      :pagination="true"
      :from="0"
      :size="10"
      :showResultStats="true"
      className="result-list-container"
      :react="{ and: ['Sentsum', 'Emosum'] }"
     :renderData="reviewsList"/>
    </ReactiveBase>
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

  .left-bar {
    float: left;
    -ms-flex-direction: column;
    flex-direction: column;
    width: 20%;
    background-color: #ffffff;
    border: 2px solid #ffffff;
    -webkit-box-shadow: 9px 10px 20px -10px #ffffff;
    box-shadow: 9px 10px 20px -10px #ffffff;
    border-radius: 5px;
    color: #000000;
    margin-left: 0;
    min-width: 200px;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    padding: 0px 10px 10px 10px;
    margin-right: 15px;
    left: 0;
    margin-top: 4px;
    margin-bottom: 10px;
  }
</style>
