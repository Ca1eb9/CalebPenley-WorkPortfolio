/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package compsci_221_pa3_cp;

/**
 *
 * @author calebpenley
 */
//UnsecuredLoan class is a subclass of LoanAccount and uses inheritance for high efficacy
public class UnsecuredLoan extends LoanAccount {
    //constructor
    public UnsecuredLoan(double new_principal, double annual_int_rate, int months){
        super(new_principal, annual_int_rate, months);
    }
    //string method to display info
    public String toString() {
        return "Unsecured Loan"+super.toString()+"\n";
    }
}