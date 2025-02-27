import { registry } from "@web/core/registry";
const actionRegistry = registry.category("actions");
const loadJsAction = async (env,context) => {
// Custom JS Code Here
console.log('JS File Loaded === Custom Script Will Execute Here',env,context);
window.alert('Java Script Alert is Running');
};
actionRegistry.add("js_code", loadJsAction);