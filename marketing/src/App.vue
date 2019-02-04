<template>
  <div id="app">
    <b-navbar toggleable="md" type="dark" variant="dark">

    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

    <b-navbar-brand href="#"><img src="./assets/logo.png" class="d-inline-block align-center " width=50px height=auto>Marketing AI</b-navbar-brand>

    <b-collapse is-nav id="nav_collapse">

      <b-navbar-nav>
        <b-nav-item href="#">reviews</b-nav-item>
        <b-nav-item href="#" disabled>Disabled</b-nav-item>
        <b-nav-item-dropdown right>
          <!-- Using button-content slot -->
          <template slot="button-content">
            <em>menu</em>
          </template>
          <b-dropdown-item href="#">drop</b-dropdown-item>
          <b-dropdown-item href="#">down</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
    <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown text="dropdown" right>
          <b-dropdown-item href="#">드</b-dropdown-item>
          <b-dropdown-item href="#">롭</b-dropdown-item>
          <b-dropdown-item href="#">다</b-dropdown-item>
          <b-dropdown-item href="#">운</b-dropdown-item>
        </b-nav-item-dropdown>
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search"/>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
    <router-view/>
  </div>
</template>

<script>
  import Vue from 'vue'
  import BootstrapVue from 'bootstrap-vue'
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'

  Vue.use(BootstrapVue);

export default {
  name: 'App'
}
</script>

<style>

@import url('https://fonts.googleapis.com/css?family=Ubuntu');

#app {
  /*font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
  font-family: 'Ubuntu', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
