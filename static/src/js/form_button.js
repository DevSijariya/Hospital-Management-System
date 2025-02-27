import { FormController } from "@web/views/form/form_controller";
import { formView } from '@web/views/form/form_view';
import { registry } from '@web/core/registry';
import { useService } from "@web/core/utils/hooks";
import {redirect} from "@web/core/utils/urls"

export class PatientFormController extends FormController {   
    setup() {
        super.setup();
        this.notificationService = useService("notification");
        this.orm = useService("orm");

     }   
     async onRecordSaved(record) { 
        const value= await super.onRecordSaved(record)
        this.notificationService.add(("Your Data Saved Successfully"), {
            title: "Success",
            type: "success"
        });
        return value;
      }
     async OnTestClick() {  
            let form_data=this.model.root.data;
            const params={
                name:form_data.name,
                email_address:form_data.email_address,
                mobile_number:form_data.mobile_number,
                address:form_data.address,
                date_of_birth:form_data.date_of_birth
            }

            console.log(form_data)
            console.log(params)
            
            this.notificationService.add(("Data Saved Successfully"), {
                title: "Success",
                type: "success"
            });
            this.orm.call("patients.description", "create",['',params]);
            return redirect("/odoo")
                        
            }

        }
        PatientFormController.template = 'save_button.form_view';
        export const modelInfoView = {   
            ...formView,   Controller: PatientFormController,};
            registry.category("views").add("button_in_form", modelInfoView);
