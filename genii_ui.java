import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class genii_ui {
   private JFrame mainFrame;
   private JLabel headerLabel;
   private JPanel controlPanel;

   public genii_ui(){
      prepareGUI();
   }

   private void prepareGUI(){
      mainFrame = new JFrame("GENII UI");
      mainFrame.setSize(400, 150);
      mainFrame.setLayout(new GridLayout(3, 1));
      headerLabel = new JLabel("",JLabel.CENTER );
      mainFrame.addWindowListener(new WindowAdapter() {
         public void windowClosing(WindowEvent windowEvent){
            System.exit(0);
         }
      });
      controlPanel = new JPanel();
      controlPanel.setLayout(new FlowLayout());

      mainFrame.add(headerLabel);
      mainFrame.add(controlPanel);
      mainFrame.setVisible(true);
   }

   private void showEventDemo(){
     headerLabel.setText("Genii Restaurant Clustering: Results Display");
     //JButton browse1=new JButton("Data File");
     JButton browse2=new JButton("Cluster File");
     JButton quit=new JButton("Quit!");
     quit.addActionListener(new ActionListener(){
       public void actionPerformed(ActionEvent arg0){
         System.exit(1);
       }
     });
     /*
     browse1.addActionListener(new ActionListener(){
       public void actionPerformed(ActionEvent arg0){
         String name=localFile();
         if(name==null) return;
         //checking the file type
         if(name.endsWith(".csv")){
           JOptionPane.showMessageDialog(mainFrame.getComponent(0), name);
           //do something with the file
           try{
             process o=new process();
             o.getLines(name);
             //mainFrame.setVisible(false);
           }catch(Exception e){}
         }
         else{
           //displaying the browser again if the file selected was not an image
           JOptionPane.showMessageDialog(mainFrame.getComponent(0), "SELECT A CSV FILE!");
           localFile();
         }
       }
     });
     */
     browse2.addActionListener(new ActionListener(){
       public void actionPerformed(ActionEvent arg0){
         String name=localFile();
         if(name==null) return;
         //checking the file type
         if(name.length()!=0){
           JOptionPane.showMessageDialog(mainFrame.getComponent(0), name);
           //do something with the file
           try{
             process o=new process();
             o.clusterProcess(name);
             mainFrame.setVisible(false);
           }catch(Exception e){
             System.out.println("NO");
           }
         }
       }
     });
     //controlPanel.add(browse1);
     controlPanel.add(browse2);
     controlPanel.add(quit);
     mainFrame.setVisible(true);
   }

   public String localFile(){
    JFileChooser chooser = new JFileChooser();
    chooser.setDialogTitle("Find Cluster File");
    chooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
    chooser.setAcceptAllFileFilterUsed(false);
    if(chooser.showOpenDialog(null)==JFileChooser.APPROVE_OPTION) {
      String name=chooser.getSelectedFile().toString();
      return name;
    }
    return null;
  }

   public static void main(String[] args){
      genii_ui swingControlDemo = new genii_ui();
      swingControlDemo.showEventDemo();
   }
}
