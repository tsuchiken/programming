   M S B A M L   `   `   `  ����  	StopWatch    StopWatch.MainWindow   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   -   5          � Title$  	StopWatch��5   	   $	��240��6   $	��400��6(   ���	#02FFFFFF���	#00000000 � WindowStyle$
 None=�6b    � AllowsTransparency . .��5	      � ���	#00000000.+�5
   
   �� -   5         ��Name$ StartButton��5
      $��Start��6&   $��26,84,275,126q�66   ���	#7F0FD2E6���	#FF14464B
���   �$��16(�6�   6�   �� 5   
   -   5        $ 	LapButton��5      $	��Lap��6$   $��26,125,275,85q�62   ���	#7F0FD2E6���	#FF14464B$��16(�6x   6�   �� 5   
   -   5        $ 
StopButton��5      $
��Stop��6%   $��141,84,160,126q�64   ���	#7F0FD2E6���	#FF14464B$��16(�6{   6�   �� 5   
   -   5        $ 
ExitButton��5      $��18��6%   $��18��60   $��382,0,0,222q�6<   ���	#CCE64B4B6h   �� 5   
   -   5         ��Name$ 	TimeLabel��5      $��28,35,226,167q�6#   ��6:   �� *ts+ �� Mode$ OneWay=� �� NotifyOnTargetUpdated . �� 5   
   -   5        $ LapTimeLabel��5      $	��120��6&   $��
257,23,0,0q�62   $��Lap Time��6F   $
��Left=�6Y   $	��Top=�6t   �� 5   
   -   5        $ LapTime��5      $	��120��6!   $��
257,49,0,0q�6-   $
��Left=�6�   $	��Top=�6�   $	��177��6�   ���	#19FFFFFF��6A   �� *	LapList+$ OneWay=� . 6�   �� 5   
   -	   5        $ Lap_RestartButton��5      $��Lap&Restart��6,   $��141,125,160,85q�6F   ���	#7F0FD2E6���	#FF14464B$��16(�6�   6�   5      5      