const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "/", component: () => import("pages/Dashboard.vue") },
      { path: "/login", component: () => import("pages/LoginPage.vue") },
      {
        path: "/register",
        component: () => import("pages/RegistrationPage.vue"),
      },
      {
        path: "/tasks",
        component: () => import("pages/Tasks.vue"),
      },
      {
        path: "/projects",
        component: () => import("pages/Projects.vue"),
      },
      {
        path: "/activity",
        component: () => import("pages/Activity.vue"),
      },
      {
        path: "/teams",
        component: () => import("pages/Teams.vue"),
      },
      {
        path: "/messages",
        component: () => import("pages/Messages.vue"),
      },
      {
        path: "/settings",
        component: () => import("pages/Settings.vue"),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes
