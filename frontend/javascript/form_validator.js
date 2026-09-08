class FormValidator {
    constructor() {
        this.rules = {};
        this.errors = {};
    }

    addRule(field, ruleFn, message) {
        if (!this.rules[field]) {
            this.rules[field] = [];
        }
        this.rules[field].push({ ruleFn, message });
    }

    validate(data) {
        this.errors = {};
        
        for (const field in this.rules) {
            const fieldRules = this.rules[field];
            const value = data[field];
            
            for (const rule of fieldRules) {
                if (!rule.ruleFn(value)) {
                    if (!this.errors[field]) {
                        this.errors[field] = [];
                    }
                    this.errors[field].push(rule.message);
                }
            }
        }
        
        return Object.keys(this.errors).length === 0;
    }

    getErrors(field = null) {
        if (field) {
            return this.errors[field] || [];
        }
        return this.errors;
    }

    hasErrors() {
        return Object.keys(this.errors).length > 0;
    }
}

const validators = {
    required: (message = "This field is required") => {
        return { ruleFn: value => value !== undefined && value !== null && value !== "", message };
    },
    
    email: (message = "Invalid email address") => {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return { ruleFn: value => !value || emailRegex.test(value), message };
    },
    
    minLength: (length, message = null) => {
        const msg = message || `Must be at least ${length} characters`;
        return { ruleFn: value => !value || value.length >= length, message: msg };
    },
    
    maxLength: (length, message = null) => {
        const msg = message || `Must be no more than ${length} characters`;
        return { ruleFn: value => !value || value.length <= length, message: msg };
    },
    
    numeric: (message = "Must be a number") => {
        return { ruleFn: value => !value || !isNaN(value), message };
    },
    
    min: (min, message = null) => {
        const msg = message || `Must be at least ${min}`;
        return { ruleFn: value => !value || Number(value) >= min, message: msg };
    },
    
    max: (max, message = null) => {
        const msg = message || `Must be no more than ${max}`;
        return { ruleFn: value => !value || Number(value) <= max, message: msg };
    }
};

const form = new FormValidator();

form.addRule("username", validators.required().ruleFn, "Username is required");
form.addRule("username", validators.minLength(3).ruleFn, "Username too short");
form.addRule("email", validators.required().ruleFn, "Email is required");
form.addRule("email", validators.email().ruleFn, "Invalid email");
form.addRule("age", validators.numeric().ruleFn, "Age must be numeric");
form.addRule("age", validators.min(18).ruleFn, "Must be 18 or older");

const testData = {
    username: "jo",
    email: "not-an-email",
    age: "16"
};
