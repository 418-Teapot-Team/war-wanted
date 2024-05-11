import { vMaska } from 'maska';
export default {
  install(app) {
    app.directive('maska', vMaska);
  },
};
