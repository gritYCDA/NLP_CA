import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import File from '@/components/File'
import Search from '@/components/Search'
import Auth from '@/components/Auth'
import Emotion from '@/components/Emotion'
import Sentiment from '@/components/Sentiment'

Vue.use(Router)

export default new Router({
  routes: [
   {
      path: '/upload',
      name: 'File',
      component: File
    },
    {
      path:'/Auth',
      name:'Auth',
      component: Auth
    },
    {
      path: '/',
      name: 'fileup',
      component: File
    },
    {
      path: '/Main',
      name: 'Main',
      component: Main
    },
    {
      path: '/Search',
      name: 'Search',
      component: Search
    },
     {
      path: '/Emotion',
      name: 'Emotion',
      component: Emotion
    },
    {
      path: '/Sentiment',
      name: 'Sentiment',
      component: Sentiment
    }
  ]
})
