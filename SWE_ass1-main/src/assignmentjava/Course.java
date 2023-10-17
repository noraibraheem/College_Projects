/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package assignmentjava;
import java.util.Vector;
import java.util.Enumeration;
/**
 *
 * @author Administrator
 */
public class Course {

    private String title;
    private Vector courseRecords;

    Course() {
        courseRecords = new Vector();
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String t) {
        title = t;
    }

    public void addCourseRecord(CourseRecord cr) {
        courseRecords.addElement(cr);
    }

    public Enumeration getCourseRecords() {
        return courseRecords.elements();
    }

    public void printCourseStudents() {
        for (Object courseRecord :
                courseRecords
        ) {
            CourseRecord temp = (CourseRecord) courseRecord;

            System.out.println(temp.getStudent());
        }
    }

    public void printBestStudent() throws NotYetSetException  {
        CourseRecord bestStudentRecord = (CourseRecord) courseRecords.get(0);

        for (int i = 1; i < courseRecords.size(); i++) {
            CourseRecord temp = (CourseRecord) courseRecords.get(i);
            if (temp.average() > bestStudentRecord.average()) {
                bestStudentRecord = temp;
            }
            System.out.println(bestStudentRecord.getStudent());
        }
    }

    public void printFinalExamStudents() {
        for (Object courseRecord : courseRecords) {
            CourseRecord record = (CourseRecord) courseRecord;
            if (record.canTakeFinalExam()) {
                System.out.println(record.getStudent());
            }
        }

    }

}

