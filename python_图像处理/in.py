#!encoding:gbk
import tkinter as tk  
window=tk.Tk()  
window.title('my window')  
window.geometry('200x200')  
e=tk.Entry(window,show=None)  
# Entry�ĵ�һ�������Ǹ����ڣ��������window  
# *��ʾ������ı���Ϊ�Ǻţ���Entry���ɼ����ݣ���ΪNone���ʾΪ�����ı���ԭ��ʽ�ɼ�  
e.pack()  
def insert_point():  
    var=e.get()
    t.insert('insert',var)  
def insert_end():
    var=e.get()
    t.insert('end',var)
#�����end��ʾ�����ڽ�β�����Ի�Ϊ1.2��������ڵ�һ�еڶ�λ����  
b1=tk.Button(window,text='insert point',width=15,height=2,command=insert_point)  
b1.pack()  
b2=tk.Button(window,text='insert end',width=15,height=2,command=insert_end)  
b2.pack()  
t=tk.Text(window,height=2)     #���������ı���ߣ�������������  
t.pack()  
window.mainloop()  