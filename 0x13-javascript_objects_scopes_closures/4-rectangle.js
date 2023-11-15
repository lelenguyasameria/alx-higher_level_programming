#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
            return {};
        }

        this.width = w;
        this.height = h;
    }

    print() {
        if (!this.width || !this.height) {
            console.log("Invalid rectangle");
            return;
        }

        for (let i = 0; i < this.height; i++) {
            console.log("X".repeat(this.width));
        }
    }

    rotate() {
        if (!this.width || !this.height) {
            console.log("Invalid rectangle");
            return;
        }

        [this.width, this.height] = [this.height, this.width];
    }

    double() {
        if (!this.width || !this.height) {
            console.log("Invalid rectangle");
            return;
        }

        this.width *= 2;
        this.height *= 2;
    }
}

const rectangle1 = new Rectangle(4, 3);
rectangle1.print();
rectangle1.rotate();
rectangle1.print();
rectangle1.double();
rectangle1.print();

const invalidRectangle = new Rectangle(0, 5);
invalidRectangle.print();

