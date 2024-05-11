import ToastPlugin from 'vue-toast-notification';
// Import one of the available themes
//import 'vue-toast-notification/dist/theme-default.css';
import 'vue-toast-notification/dist/theme-bootstrap.css';

export default {
  install(app) {
    app.use(ToastPlugin, {
      queue: true,
    });
  },
};
