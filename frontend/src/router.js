import { createWebHistory, createRouter } from "vue-router";
import Home from "@/views/Home.vue";
import Signup from "@/views/Signup.vue";
import Signin from "@/views/Signin.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      authRequired: true
    }
  },
  {
    path: "/signup",
    name: "signup",
    component: Signup,
  },
  {
    path: "/signin",
    name: "signin",
    component: Signin,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.authRequired)) {
      next({path: '/signin'});
  } else {
      next();
  }
});

export default router;