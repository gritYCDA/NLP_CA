<template>
 <v-container grid-list-md>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex xs12 sm8 lg4 md5>
          <v-card class="login-card">
            <v-card-title>
              <span class="headline">Upload File</span>
            </v-card-title>

            <v-spacer/>

            <v-card-text>

              <v-layout
                row
                fill-height
                justify-center
                align-center
                v-if="loading"
              >
                <v-progress-circular
                  :size="50"
                  color="primary"
                  indeterminate
                />
              </v-layout>


              <v-form v-else ref="form" v-model="valid" lazy-validation>
                <v-container>
                  <div class="inputTitle">Project Name :</div>
                  <input class="form-control" type="text" name="projectName" v-model="projectName"><br/>
                  <div class="inputTitle">Project File :  </div>
                  <input class="form-control" type="file" name="file" id="file" ref="file" v-on:change="handleFileUpload()"/><br/>
                  <v-btn href="/#/Main" class="pink white--text" :disabled="!valid"  @click="submitFile">Submit</v-btn>
                 </v-container>
              </v-form>


            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
  import axios from 'axios';
  export default {
    name: 'File',
    data() {
      return {
        projectName: null, 
        projectFile: null
      }
    },
    methods: {
      submitFile() { //Function
        console.log("submit file")
        if (this.projectName) {
          let formData = new FormData();
          formData.set('projectName',this.projectName);
          formData.append('projectFile', this.file);

          axios({
            method:'post',
            url: 'http://localhost:8000/uploads/',
            data: formData,
            headers: {
              'Content-Type': 'multipart/form-data'
            },
            auth: { // Basic authentication
              username: 'admin',
              password: 'admin123!'
            }
          }).then((response) => {
            console.log("SUCCESS")
          })
          .catch((error) => {
            console.log(error);
        });
      }
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    }
  }
}
</script>
<style>
.inputTitle {
  text-align: left;
}

</style>
