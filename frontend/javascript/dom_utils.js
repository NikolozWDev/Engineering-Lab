class DOM {
    static select(selector, parent = document) {
        return parent.querySelector(selector);
    }

    static selectAll(selector, parent = document) {
        return [...parent.querySelectorAll(selector)];
    }

    static create(tag, options = {}) {
        const el = document.createElement(tag);
        
        if (options.className) el.className = options.className;
        if (options.id) el.id = options.id;
        if (options.text) el.textContent = options.text;
        if (options.html) el.innerHTML = options.html;
        
        if (options.attrs) {
            for (const [key, value] of Object.entries(options.attrs)) {
                el.setAttribute(key, value);
            }
        }
        
        if (options.style) {
            Object.assign(el.style, options.style);
        }
        
        if (options.children) {
            options.children.forEach(child => el.appendChild(child));
        }
        
        return el;
    }

    static on(element, event, handler, options = {}) {
        element.addEventListener(event, handler, options);
        return () => element.removeEventListener(event, handler, options);
    }

    static delegate(parent, selector, event, handler) {
        const listener = (e) => {
            const target = e.target.closest(selector);
            if (target && parent.contains(target)) {
                handler.call(target, e, target);
            }
        };
        parent.addEventListener(event, listener);
        return () => parent.removeEventListener(event, listener);
    }

    static addClass(element, ...classes) {
        element.classList.add(...classes);
    }

    static removeClass(element, ...classes) {
        element.classList.remove(...classes);
    }

    static toggleClass(element, className, force) {
        return element.classList.toggle(className, force);
    }

    static hasClass(element, className) {
        return element.classList.contains(className);
    }

    static show(element, display = 'block') {
        element.style.display = display;
    }

    static hide(element) {
        element.style.display = 'none';
    }

    static empty(element) {
        while (element.firstChild) {
            element.removeChild(element.firstChild);
        }
    }

    static remove(element) {
        if (element.parentNode) {
            element.parentNode.removeChild(element);
        }
    }
}

const container = DOM.create('div', {
    className: 'container',
    style: { padding: '20px' }
});

const title = DOM.create('h1', {
    text: 'Hello World',
    style: { color: 'blue' }
});

const list = DOM.create('ul', {
    className: 'items',
    children: [
        DOM.create('li', { text: 'Item 1', attrs: { 'data-id': '1' } }),
        DOM.create('li', { text: 'Item 2', attrs: { 'data-id': '2' } })
    ]
});
