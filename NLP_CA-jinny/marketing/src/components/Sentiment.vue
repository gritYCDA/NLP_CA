<template>
  <div>
    <h1>Sentiment Analysis Summary</h1>
    <br>
    <div>
      <GChart
        align="center"
      type="ColumnChart"
      :data="chartData2"
      :options="chartOptions2"
      />
    </div>
    <br>
    <div class="col-md-12">
      <div class="col-md-4">
        <h3>POSITIVE</h3>
        <div>
          <h1 class="emoji">👍</h1>
        </div>
        <h2>19</h2>
      </div>
      <div class="col-md-4">
        <h3>NEUTRAL</h3>
        <div>
          <h1 class="emoji">👊</h1>
        </div>
        <h2>24</h2>
      </div>
      <div class="col-md-4">
        <h3>NEGATIVE</h3>
        <div>
          <h1 class="emoji">👎</h1>
        </div>
        <h2>47</h2>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
      name: "sentimental-bar",
      data() {
        return {
          // Array will be automatically processed with visualization.arrayToDataTable function

          chartData2: [
            ['Sentiment', 'Num of Reviews'],
            ['Negative', 47],
            ['Neutral', 24],
            ['Positive', 19],
          ],
          chartOptions2: {
            title: 'Sentiment of Reviews',
            width: 900,
            legend: {position: 'none'},
            chart: {
              title: 'Sentiment of Reviews',
              subtitle: 'number of reviews'
            },
            bars: 'vertical', // Required for Material Bar Charts.
            axes: {
              x: {
                0: {side: 'top', label: 'Number of Reviews'} // Top x-axis.
              }
            },
            bar: {groupWidth: "90%"}
          }
        }
      }
    }
</script>

<style scoped>
  .col-md-12 {
    display: block;
    content: '';
    clear: both;
  }
  .col-md-4 {
    float: left;
  }
  .emoji {
    font-size: 100px;
  }
</style>
