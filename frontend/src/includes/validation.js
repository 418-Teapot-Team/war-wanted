import {
  Form as VeeForm,
  Field as VeeField,
  defineRule,
  ErrorMessage,
  configure,
} from 'vee-validate';
import {
  required,
  min,
  max,
  alpha_spaces as alphaSpaces,
  email,
  min_value as minVal,
  max_value as maxVal,
  confirmed,
} from '@vee-validate/rules';

export default {
  install(app) {
    app.component('VeeForm', VeeForm);
    app.component('VeeField', VeeField);
    app.component('ErrorMessage', ErrorMessage);

    defineRule('required', required);
    defineRule('min', min);
    defineRule('max', max);
    defineRule('alpha_spaces', alphaSpaces);
    defineRule('email', email);
    defineRule('min_value', minVal);
    defineRule('max_value', maxVal);
    defineRule('passwords_mismatch', confirmed);

    configure({
      generateMessage: (ctx) => {
        const messages = {
          required: `*Це поле обов'язкове`,
          min: `*Недостаньо символів`,
          max: `*Перевищено максимальну к-кість символів`,
          alpha_spaces: `*Це поле може містити лише букви та пробіли`,
          email: `*Неправильний формат емейлу`,
          min_value: `The field ${ctx.field} is too low.`,
          max_value: `The field ${ctx.field} is too high.`,
          passwords_mismatch: `*Паролі не співпадають`,
        };

        const message = messages[ctx.rule.name] ? messages[ctx.rule.name] : `*Поле некоректне`;

        return message;
      },
      validateOnBlur: true,
      validateOnChange: true,
      validateOnInput: false,
      validateOnModelUpdate: true,
    });
  },
};
