export function parse(qs) {
    const result = {};
    const params = new URLSearchParams(qs.startsWith('?') ? qs.slice(1) : qs);
    for (const [key, value] of params) {
        result[key] = value;
    }
    return result;
}

export function build(obj) {
    const params = new URLSearchParams();
    for (const [key, value] of Object.entries(obj)) {
        if (value !== undefined && value !== null) {
            params.append(key, value);
        }
    }
    return params.toString();
}

if (import.meta.url === `file://${process.argv[1]}`) {
    console.log(parse("?a=1&b=hello&c=x"));
    console.log(build({ a: 1, b: "hello world", skip: null }));
}
