const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "/", component: () => import("pages/Dashboard.vue"),meta: { requiresAuth: true } },
      {
        path: "/tasks",
        component: () => import("pages/Tasks.vue"), meta: { requiresAuth: true }
      },
      {
        path: "/projects",
        component: () => import("pages/Projects.vue"), meta: { requiresAuth: true }
      },
      {
        path: "/activity",
        component: () => import("pages/Activity.vue"), meta: { requiresAuth: true }
      },
      {
        path: "/teams",
        component: () => import("pages/Teams.vue"), meta: { requiresAuth: true }
      },
      {
        path: "/messages",
        component: () => import("pages/Messages.vue"), meta: { requiresAuth: true }
      },
      {
        path: "/settings",
        component: () => import("pages/Settings.vue"), meta: { requiresAuth: true }
      },
    ],
  },
  { path: "/login", component: () => import("pages/LoginPage.vue") },
  {
    path: "/register",
    component: () => import("pages/RegisterPage.vue"),
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes
