<template>
  <div>
<div>
    <br><br>
    <b-card-group deck>

      <b-card size="lg" bg-variant="primary" text-variant="white" class="text-center">
        <a href="/#/upload">
        <img src="https://img.icons8.com/ios/100/000000/file.png">
        <br></a>
        <b-card-text>File Upload</b-card-text>
      </b-card>


      <b-card bg-variant="info" text-variant="white" class="text-center">
         <a href="/#/Sentiment">
        <img src="https://img.icons8.com/ios/100/000000/thumb-up.png"><br>
           </a>
        <b-card-text >Analyze Sentiment</b-card-text>
      </b-card>

    </b-card-group>
  </div>
    <br>
  <div>
    <b-card-group deck>

      <b-card bg-variant="warning" text-variant="white" class="text-center" >
        <a href ="/#/Emotion">
      <img src="https://img.icons8.com/ios/100/000000/happy.png"><br>
          </a>
        <b-card-text>Analyze Emotion</b-card-text>
      </b-card>


      <b-card bg-variant="danger" text-variant="white" class="text-center">
        <a href="/#/Search">
        <img src="https://img.icons8.com/ios/100/000000/search-filled.png"><br>
          </a>
        <b-card-text>Reviews</b-card-text>
      </b-card>
    </b-card-group>
  </div>
    </div>
</template>

<script>
    export default {
        name: "main",

    }
</script>

<style scoped>

</style>
