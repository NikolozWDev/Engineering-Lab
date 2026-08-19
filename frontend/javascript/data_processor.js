class DataProcessor {
    constructor(data = []) {
        this.data = data;
    }

    filterByCondition(conditionFn) {
        return this.data.filter(conditionFn);
    }

    sortByField(field, ascending = true) {
        return [...this.data].sort((a, b) => {
            if (a[field] < b[field]) return ascending ? -1 : 1;
            if (a[field] > b[field]) return ascending ? 1 : -1;
            return 0;
        });
    }

    groupByField(field) {
        const groups = {};
        this.data.forEach(item => {
            const key = item[field];
            if (!groups[key]) {
                groups[key] = [];
            }
            groups[key].push(item);
        });
        return groups;
    }

    getStatistics(field) {
        const values = this.data.map(item => item[field]).filter(v => typeof v === 'number');
        if (values.length === 0) return null;

        const sum = values.reduce((acc, val) => acc + val, 0);
        return {
            min: Math.min(...values),
            max: Math.max(...values),
            average: sum / values.length,
            sum: sum
        };
    }

    transformData(transformFn) {
        return this.data.map(transformFn);
    }

    findDuplicates(field) {
        const seen = new Map();
        const duplicates = [];

        this.data.forEach(item => {
            const key = item[field];
            if (seen.has(key)) {
                duplicates.push(item);
            } else {
                seen.set(key, true);
            }
        });

        return duplicates;
    }
}

const sampleData = [
    { id: 1, name: "Alice", age: 25, salary: 50000 },
    { id: 2, name: "Bob", age: 30, salary: 60000 },
    { id: 3, name: "Charlie", age: 35, salary: 70000 },
    { id: 4, name: "Diana", age: 28, salary: 55000 },
    { id: 5, name: "Eve", age: 32, salary: 65000 }
];

const processor = new DataProcessor(sampleData);
