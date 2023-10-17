/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package assignmentjava;

/**
 *
 * @author Administrator
 */
public class Assignment {
private double mark = -1;

    Assignment() {
    }
    Assignment(double mark) {
        this.mark=mark;
    }

    public double getMark() throws NotYetSetException {
        if (mark == -1) {
            throw new NotYetSetException("Mark is not yet set");
        }
        return mark;
    }

    public void setMark(double m) {
        mark = m;
    }

    // implemented to help in CourseRecord class.
    public boolean hasMark() {
        if (mark > -1)
            return true;
        else
            return false;
    }
}
