"use strict";define(["underscore","module","views/shared/controls/Control","splunk.util"],function(a,b,c,d){var e=c.extend({className:"control",moduleId:b.id,initialize:function(){var b={buttonClassName:"btn",defaultValue:!0,label:""};a.defaults(this.options,b),this.options.modelAttribute&&this.$el.attr("data-name",this.options.modelAttribute),c.prototype.initialize.apply(this,arguments)},events:{"click button":function(a){!this.options.enabled||this.setValue(!this._value),a.preventDefault()}},disable:function(){this.options.enabled=!1},enable:function(){this.options.enabled=!0},normalizeValue:function(a){return d.normalizeBoolean(a)?1:0},render:function(){var a=this.options.invertValue?!this.getValue():this.getValue();if(!this.el.innerHTML){var b=this.template_button({options:this.options,clicked:a});""!==this.options.count&&this.$el.html(b),this.options.enabled||this.disable()}var c=this.options.additionalClassNames;return c&&this.$el.addClass(c),this},template_button:a.template('\n            <button type="button" value="<%- options.label %>" class="syn-btn-label <%- options.buttonClassName %> <% if(options.isSelected){%>active<%}%>">\n                <span class="syn-left-label">\n                <% if (options.label == "informational") { %>\n                <%- _("INFO").t() %>\n                <% } else { %>\n                <%- _(options.label.toUpperCase()).t() %>\n                <% } %>\n                </span>\n                <span class="syn-right-label">\n                <%- options.count %>\n                </span>\n            </button>\n        ')});return e});