<template>
  <div>
    <h1>Emotion Analysis Summary</h1>
    <br>
    <div>
      <GChart
    align="center"
    type="ColumnChart"
    :data="chartData1"
    :options="chartOptions1"
  />
    </div>
    <br>
    <div class="col-md-12">
      <div class="col-md-4">
        <h3>HAPPY</h3>
        <div>
          <h1 class="emoji">😊</h1>
        </div>
        <h2>4</h2>
      </div>
      <div class="col-md-4">
        <h3>ANGRY</h3>
        <div>
          <h1 class="emoji">😡</h1>
        </div>
        <h2>15</h2>
      </div>
      <div class="col-md-4">
        <h3>EXCITED</h3>
        <div>
          <h1 class="emoji">🤩</h1>
        </div>
        <h2>42</h2>
      </div>
    </div>
    <br><br>
    <div class="col-md-12">
      <div class="col-md-3">
        <h3>SAD</h3>
        <div>
          <h1 class="emoji">😭</h1>
        </div>
        <h2>1</h2>
      </div>
      <div class="col-md-3">
        <h3>BORED</h3>
        <div>
          <h1 class="emoji">😒</h1>
        </div>
        <h2>11</h2>
      </div>
      <div class="col-md-3">
        <h3>AFRAID</h3>
        <div>
          <h1 class="emoji">😯</h1>
        </div>
        <h2>4</h2>
      </div>
      <div class="col-md-3">
        <h3>DISGUST</h3>
          <h1 class="emoji">🤮</h1>
        </div>
        <h2>3</h2>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "analyze",
      data () {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData1: [
        ['Emotion', 'Num of Reviews'],
        ['Happy', 4],
        ['Angry', 15],
        ['Excited', 42],
        ['Sad', 1],
        ['Bored', 11],
        ['Afraid', 14],
        ['Disgust', 3],
      ],
      chartOptions1: {
        title: 'Emotion of Reviews',
          width: 900,
          legend: { position: 'none' },
          chart: { title: 'Emotion of Reviews',
                   subtitle: 'number of reviews' },
          bars: 'vertical', // Required for Material Bar Charts.
          axes: {
            x: {
              0: { side: 'top', label: 'Number of Reviews'} // Top x-axis.
            }
          },
          bar: { groupWidth: "90%" }
      },
      //  chartData2: [
      //   ['Sentiment', 'Num of Reviews'],
      //   ['Negative', 47],
      //   ['Neutral', 24],
      //   ['Positive', 19],
      // ],
      // chartOptions2: {
      //   title: 'Sentiment of Reviews',
      //     width: 900,
      //     legend: { position: 'none' },
      //     chart: { title: 'Sentiment of Reviews',
      //              subtitle: 'number of reviews' },
      //     bars: 'vertical', // Required for Material Bar Charts.
      //     axes: {
      //       x: {
      //         0: { side: 'top', label: 'Number of Reviews'} // Top x-axis.
      //       }
      //     },
      //     bar: { groupWidth: "90%" }
      // }
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
  .col-md-3 {
    float: left;
  }
  .emoji {
    font-size: 100px;
  }
</style>
