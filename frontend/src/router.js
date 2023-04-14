import { createWebHistory, createRouter } from "vue-router";
import Welcome from "@/views/Welcome.vue";
import Signup from "@/views/Signup.vue";
import Signin from "@/views/Signin.vue";
import Dashboard from "@/views/Dashboard.vue";
import AllQuestions from "@/views/AllQuestions.vue";
import Question from "@/views/Question.vue";

const routes = [
  {
    path: "/",
    component: Welcome
  },
  {
    path: "/welcome",
    name: "Welcome",
    component: Welcome
  },
  {
    path: "/signup",
    name: "signup",
    component: Signup,
  },
  {
    path: "/signin",
    name: "Signin",
    component: Signin,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: {
      authRequired: true
    }
  },
  {
    path: "/allquestions",
    name: "AllQuestions",
    component: AllQuestions,
    meta: {
      authRequired: true
    }
  },
  {
    path: "/question/:id",
    name: "Question",
    component: Question,
    meta: {
      authRequired: true
    }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  let signedIn = true

  if (to.path == '/') {
    if (signedIn) {
      next('/dashboard')
    } else {
      next('/welcome')
    }
  }

  if (to.matched.some(record => record.meta.authRequired)) {
    if (!signedIn) {
      next({path: '/'});
    } else {
      next();
    }
  } else {
      next();
  }
});

export default router;