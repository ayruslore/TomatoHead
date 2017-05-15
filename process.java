import java.io.*;
import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class process{
  ArrayList<String>lines;
  ArrayList<Integer>c;
  private JFrame mainFrame;
  private JLabel headerLabel;
  private JPanel controlPanel;
  int numOfClusters;

  public void getLines()throws IOException{
    BufferedReader br=new BufferedReader(new FileReader("Tomato Head.csv"));
    lines=new ArrayList<String>();
    String line=null;
    while((line=br.readLine())!=null)
      lines.add(line);
  }

  public void clusterProcess(String fileName)throws FileNotFoundException{
    try{
      getLines();
    }catch(Exception e){}

    c=new ArrayList<Integer>();
    Scanner sc=new Scanner(new File(fileName));
    int maxNumber=0, count=0;
    while(sc.hasNext()){
      int i=sc.nextInt();
      maxNumber=i>maxNumber?i:maxNumber;
      c.add(i);
      count++;
    }
    setMaxCluster(maxNumber+1);
    display();
  }

  public void setMaxCluster(int n){
    numOfClusters=n;
  }

  private void showEventDemo(){
    headerLabel.setText("Genii Restaurant Clustering: Results Display");
    JButton quit=new JButton("Quit!");
    quit.addActionListener(new ActionListener(){
      public void actionPerformed(ActionEvent arg0){
        System.exit(1);
      }
    });
    clusterDropdown();
    controlPanel.add(quit);
    mainFrame.setVisible(true);
  }

  public void display(){
    mainFrame=new JFrame("GENII UI");
    mainFrame.setSize(400, 150);
    mainFrame.setLayout(new GridLayout(3, 1));
    headerLabel = new JLabel("",JLabel.CENTER );
    mainFrame.addWindowListener(new WindowAdapter() {
       public void windowClosing(WindowEvent windowEvent){
          System.exit(0);
       }
    });
    controlPanel=new JPanel();
    controlPanel.setLayout(new FlowLayout());

    mainFrame.add(headerLabel);
    mainFrame.add(controlPanel);
    mainFrame.setVisible(true);
    showEventDemo();
  }

  public void clusterDropdown(){
    DefaultComboBoxModel clusterNum=new DefaultComboBoxModel();
    for(int i=0; i<numOfClusters; i++)
      clusterNum.addElement(i);
    final JComboBox clusterNo=new JComboBox(clusterNum);
    clusterNo.setSelectedIndex(0);
    JScrollPane cn=new JScrollPane(clusterNo);

    DefaultComboBoxModel ratingBox=new DefaultComboBoxModel();
    ratingBox.addElement("2.0");
    ratingBox.addElement("2.5");
    ratingBox.addElement("3.0");
    ratingBox.addElement("3.5");
    ratingBox.addElement("3.8");
    ratingBox.addElement("4.0");
    ratingBox.addElement("4.2");
    ratingBox.addElement("4.4");
    ratingBox.addElement("4.6");
    ratingBox.addElement("4.8");
    final JComboBox rate=new JComboBox(ratingBox);
    rate.setSelectedIndex(0);
    JScrollPane mr=new JScrollPane(rate);

    JButton show=new JButton("Show");
    show.addActionListener(new ActionListener(){
      public void actionPerformed(ActionEvent e){
        String data=null;
        String data2=null;
        clusterNum o=new clusterNum(c, lines, numOfClusters);
        o.fill();
        if(clusterNo.getSelectedIndex()!=-1)
          data=""+clusterNo.getItemAt(clusterNo.getSelectedIndex());
        if(clusterNo.getSelectedIndex()!=-1)
          data2=""+rate.getItemAt(rate.getSelectedIndex());
        String msg=o.displayCluster(Integer.parseInt(data), Float.parseFloat(data2.substring(0, 3)));
        if(msg.length()==0) msg="No such Restaurant found!";
        JOptionPane.showMessageDialog(mainFrame.getComponent(0), msg);
      }
    });
    controlPanel.add(cn);
    controlPanel.add(mr);
    controlPanel.add(show);
  }
}
