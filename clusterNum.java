import java.util.*;
import java.io.*;

class clusterNum{
  ArrayList<Integer>c;
  ArrayList<String>lines;
  node[]a;

  public clusterNum(ArrayList<Integer>c, ArrayList<String>lines, int maxNumber){
    this.c=new ArrayList<Integer>(c);
    this.lines=new ArrayList<String>(lines);
    a=new node[maxNumber];
  }

  public void fill(){
    for(int i=1; i<c.size(); i++){
      String rest=lines.get(i);
      int d1=rest.indexOf(',');
      int d2=rest.indexOf(',', d1+1);
      int d3=rest.indexOf(',', d2+1);
      float rating;
      if(rest.substring(d2+1, d3).equals("NA")) rating=0f;
      else rating=Float.parseFloat(rest.substring(d2+1, d3));
      node temp=new node(rest.substring(0, d1), rest.substring(d1+1, d2), rating);
      temp.next=a[c.get(i)];
      a[c.get(i)]=temp;
    }
  }

  public String displayCluster(int n, float r){
    String s="";
    for(node j=a[n]; j!=null; j=j.next){
      if(j.rating>=r)
        s=s+j.name+", "+j.location+", "+j.rating+"\n";
    }
    //System.out.println(s);
    return s;
  }
}
