using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.ComponentModel;

namespace StopWatch
{
    /// <summary>
    /// MainWindow.xaml の相互作用ロジック
    /// </summary>
    public partial class MainWindow : INotifyPropertyChanged
    {
        private Stopwatch sw;
        private TimeSpan ts;
        private List<TimeSpan> LapList;

        public event PropertyChangedEventHandler PropertyChanged;

        public TimeSpan timeSpan
        {
            get { return ts; }
            set
            {
                ts = sw.Elapsed;
                OnPropertyChanged("TimeSpan");
            }
        }
        
        public MainWindow()
        {
            InitializeComponent();
            sw = new Stopwatch();
            DataContext = new { ts, LapList };
            LapList = new List<TimeSpan>();
        }

        private void Window_MouseLeftButtonDown(object sender, MouseButtonEventArgs e)
        {
            this.DragMove();
        }

        private void ExitButton_Click(object sender, MouseButtonEventArgs e)
        {
            this.Close();
        }

        private void StartButton_Click(object sender, MouseButtonEventArgs e)
        {

            sw.Start();
            while (sw.IsRunning)
            {
                
                ts = sw.Elapsed;
            }
        }

        private void LapButton_Click(object sender, MouseButtonEventArgs e)
        {
            AddLap(ts);
        }

        private void StopButton_Click(object sender, MouseButtonEventArgs e)
        {
            sw.Stop();
        }

        private void Lap_RestartButton_Click(object sender, MouseButtonEventArgs e)
        {
            
            sw.Restart();
        }

        private void AddLap(TimeSpan Arg_TimeSpan)
        {
            LapList.Add(Arg_TimeSpan);
        }

        protected void OnPropertyCHanged(string ts)
        {
            PropertyChangedEventHandler handler = PropertyChanged;
        }
    }   
}
