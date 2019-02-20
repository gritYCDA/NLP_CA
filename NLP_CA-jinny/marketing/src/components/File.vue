<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">

        <label>File</label><br/>
        Project Name : <input type="text" name="projectName" v-model="projectName"><br/>
        Project File : <input type="file" name="file" id="file" ref="file" v-on:change="handleFileUpload()"/><br/>
        <button v-on:click="submitFile()">Submit</button>

    </div>
  </div>
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

