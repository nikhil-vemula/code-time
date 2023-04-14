import { createWebHistory, createRouter } from "vue-router";
import Home from "@/views/Home.vue";
import Signup from "@/views/Signup.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/signup",
    name: "signup",
    component: Signup,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;