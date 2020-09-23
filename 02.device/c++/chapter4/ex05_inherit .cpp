class Shape {
protected:
    int x, y;

public:
    void draw() {}
    void move() {}
};

class Reactangle : public Shape {
protected:
    int width;
    int height;
public:
    int calcArea()
    {
        return width * height;
    }
};