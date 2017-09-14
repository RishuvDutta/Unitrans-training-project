from django.test import TestCase
from datetime import datetime, date, time, timedelta
from django.utils.timezone import make_aware, get_default_timezone, utc
from django.db.models import Q
from shifts_app.run import Run
from shifts_app.shift import Shift
#from shifts_app.shift_group import ShiftGroup

# Some code borrowed from Bryce

class ShiftTests(TestCase):

    def set_up(self,case_num):
        runs = []
        run_times_list = []

        if case_num == 1:
            shift_start_date = date(2016,4,12)
            shift_end_date = date(2016,4,12)
            shift_start_time = time(11,00)
            shift_end_time = time(15,00)

            shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
            shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)

            shift_info = [shift_start_datetime, shift_end_datetime]
            run_times_list = [
                    {'start_time':time(11,00), 'end_time': time(12,00)}
            ]
            shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
            dummy_shift = Shift.objects.create(start_datetime=shift_start_datetime, end_datetime = shift_end_datetime)
            shift_end_datetime = make_aware(datetime.combine(shift_start_date, time(12,00)),utc)
            run = Run.objects.create(shift = dummy_shift, start_datetime = shift_start_datetime, end_datetime = shift_end_datetime)
            return (shift, shift_info, run)
        
        if case_num == 2:
            shift_start_date = date(2016,4,12)
            shift_end_date = date(2016,4,12)
            shift_start_time = time(00,00)
            shift_end_time = time(23,59)

            shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
            shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)
            total_dur = abs(shift_start_datetime.hour - shift_end_datetime.hour)
            shift_info = [shift_start_datetime, shift_end_datetime]
            runs = []
            shift_runs = []

            run_times_list = [
                {'start_time':time(12,00), 'end_time': time(13,00)}, 
                {'start_time':time(13,00),'end_time':time(14,00)},
            ]
            
            shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
            dummy_shift = Shift.objects.create(start_datetime=shift_start_datetime, end_datetime = shift_end_datetime)
            date_range = [shift_start_datetime, shift.end_datetime]
            last_end_date = shift_start_datetime.date()

            for run in shift.runs_related.all():
                shift_runs.append(run)

            for key in run_times_list:
                run_start_datetime = make_aware(datetime.combine(last_end_date, key['start_time']),utc)
                run_end_datetime =  make_aware(datetime.combine(last_end_date, key['end_time']), utc)
                if run_start_datetime > run_end_datetime:
                    run_end_datetime += timedelta(days=1)
               
                last_end_date = run_end_datetime.date()
                run = Run.objects.create(shift = dummy_shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
                runs.append(run)
        
            return (runs, shift_runs, shift, date_range) 

        if case_num == 3:
            shift_start_date = date(2016,4,12)
            shift_end_date = date(2016,4,12)
            shift_start_time = time(00,00)
            shift_end_time = time(23,59)

            shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
            shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)
            total_dur = abs(shift_start_datetime.hour - shift_end_datetime.hour)
            shift_info = [shift_start_datetime, shift_end_datetime]
            runs = []
            shift_runs = []

            run_times_list = [
                {'start_time':time(15,00), 'end_time': time(16,00)}, 
                {'start_time':time(16,00),'end_time':time(17,00)},
                {'start_time':time(17,00), 'end_time':time(18,00)},
            ]
            
            shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
            dummy_shift = Shift.objects.create(start_datetime=shift_start_datetime, end_datetime = shift_end_datetime)
            date_range = [shift_start_datetime, shift.end_datetime]
            last_end_date = shift_start_datetime.date()

            for run in shift.runs_related.all():
                shift_runs.append(run)

            for key in run_times_list:
                run_start_datetime = make_aware(datetime.combine(last_end_date, key['start_time']),utc)
                run_end_datetime =  make_aware(datetime.combine(last_end_date, key['end_time']), utc)
                if run_start_datetime > run_end_datetime:
                    run_end_datetime += timedelta(days=1)
               
                last_end_date = run_end_datetime.date()
                run = Run.objects.create(shift = dummy_shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
                runs.append(run)
        
            
            return (runs, shift_runs, shift, date_range)

        if case_num == 4:
            shift_start_date = date(2016,4,18)
            shift_end_date = date(2016,4,20)
            shift_start_time = time(00,00)
            shift_end_time = time(23,59)

            shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
            shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)
            shift_info = [shift_start_datetime, shift_end_datetime]
            runs = []
            shift_runs = []
        
            run_times_list = [
                {'start_time':time(11,00), 'end_time': time(12,00)}, 
            ]
            
            shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
            dummy_shift = Shift.objects.create(start_datetime=shift_start_datetime, end_datetime = shift_end_datetime)
            date_range = [shift_start_datetime, shift.end_datetime]
            last_end_date = shift_start_datetime.date()

            for run in shift.runs_related.all():
                shift_runs.append(run)

            for key in run_times_list:
                run_start_datetime = make_aware(datetime.combine(last_end_date, key['start_time']),utc)
                run_end_datetime =  make_aware(datetime.combine(last_end_date, key['end_time']), utc)
                if run_start_datetime > run_end_datetime:
                    run_end_datetime += timedelta(days=1)
               
                last_end_date = run_end_datetime.date()
                run = Run.objects.create(shift = dummy_shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
                runs.append(run)
        
        
            return (runs, shift_runs, shift, date_range) 

        if case_num == 5:
            shift_start_date = date(2016,4,18)
            shift_end_date = date(2016,4,20)
            shift_start_time = time(00,00)
            shift_end_time = time(23,59)

            shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
            shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)
            shift_info = [shift_start_datetime, shift_end_datetime]
            runs = []
            shift_runs = []
            run_times_list = [
                {'start_time':time(13,00), 'end_time': time(14,00)}, 
                {'start_time':time(14,00),'end_time':time(15,00)},
            ]
            
            shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
            dummy_shift = Shift.objects.create(start_datetime=shift_start_datetime, end_datetime = shift_end_datetime)
            date_range = [shift_start_datetime, shift.end_datetime]
            last_end_date = shift_start_datetime.date()

            for run in shift.runs_related.all():
                shift_runs.append(run)

            for key in run_times_list:
                run_start_datetime = make_aware(datetime.combine(last_end_date, key['start_time']),utc)
                run_end_datetime =  make_aware(datetime.combine(last_end_date, key['end_time']), utc)
                if run_start_datetime > run_end_datetime:
                    run_end_datetime += timedelta(days=1)
               
                last_end_date = run_end_datetime.date()
                run = Run.objects.create(shift = dummy_shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
                runs.append(run)
        
        
            return (runs, shift_runs, shift, date_range)  

        if case_num == 6:
            shift_start_date = date(2016,4,18)
            shift_end_date = date(2016,4,20)
            shift_start_time = time(00,00)
            shift_end_time = time(23,59)

            shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
            shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)
            shift_info = [shift_start_datetime, shift_end_datetime]
            runs = []
            shift_runs = []

            run_times_list = [
                {'start_time':time(22,30), 'end_time': time(23,30)}, 
                {'start_time':time(23,30),'end_time':time(0,30)},
                {'start_time':time(0,30),'end_time':time(1,30)},
            ]
            
            shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
            dummy_shift = Shift.objects.create(start_datetime=shift_start_datetime, end_datetime = shift_end_datetime)
            date_range = [shift_start_datetime, shift.end_datetime]
            last_end_date = shift_start_datetime.date()

            for run in shift.runs_related.all():
                shift_runs.append(run)

            for key in run_times_list:
                run_start_datetime = make_aware(datetime.combine(last_end_date, key['start_time']),utc)
                run_end_datetime =  make_aware(datetime.combine(last_end_date, key['end_time']), utc)
                if run_start_datetime > run_end_datetime:
                    run_end_datetime += timedelta(days=1)
               
                last_end_date = run_end_datetime.date()
                run = Run.objects.create(shift = dummy_shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
                runs.append(run)
        
        
            return (runs, shift_runs, shift, date_range) 

        if case_num == 7:
            shift_start_date = date(2016,4,21)
            shift_end_date = date(2016,4,23)
            shift_start_time = time(00,00)
            shift_end_time = time(23,59)

            shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
            shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)
            shift_info = [shift_start_datetime, shift_end_datetime]
            runs = []
            shift_runs = []

            run_times_list = [
                {'start_time':time(11,00), 'end_time': time(12,00)},
                {'start_time':time(12,00), 'end_time': time(13,00)}, 
                {'start_time':time(13,00), 'end_time': time(14,00)}, 
            ]
            
            shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
            dummy_shift = Shift.objects.create(start_datetime=shift_start_datetime, end_datetime = shift_end_datetime)
            date_range = [shift_start_datetime, shift.end_datetime]
            last_end_date = shift_start_datetime.date()

            for run in shift.runs_related.all():
                shift_runs.append(run)

            for key in run_times_list:
                run_start_datetime = make_aware(datetime.combine(last_end_date, key['start_time']),utc)
                run_end_datetime =  make_aware(datetime.combine(last_end_date, key['end_time']), utc)
                if run_start_datetime > run_end_datetime:
                    run_end_datetime += timedelta(days=1)
               
                last_end_date = run_end_datetime.date()
                run = Run.objects.create(shift = dummy_shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
                runs.append(run)

            return (runs, shift_runs, shift, date_range) 

        if case_num == 8:
            shift_start_date = date(2016,4,21)
            shift_end_date = date(2016,4,23)
            shift_start_time = time(00,00)
            shift_end_time = time(23,59)

            shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
            shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)
            shift_info = [shift_start_datetime, shift_end_datetime]
            runs = []
            shift_runs = []

            run_times_list = [
                {'start_time':time(20,00), 'end_time': time(3,00)},
                {'start_time':time(21,00), 'end_time': time(2,00)}, 
            ]
            
            shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
            dummy_shift = Shift.objects.create(start_datetime=shift_start_datetime, end_datetime = shift_end_datetime)
            date_range = [shift_start_datetime, shift.end_datetime]
            last_end_date = shift_start_datetime.date()

            for run in shift.runs_related.all():
                shift_runs.append(run)

            for key in run_times_list:
                run_start_datetime = make_aware(datetime.combine(last_end_date, key['start_time']),utc)
                run_end_datetime =  make_aware(datetime.combine(last_end_date, key['end_time']), utc)
                if run_start_datetime > run_end_datetime:
                    run_end_datetime += timedelta(days=1)
               
                last_end_date = run_end_datetime.date()
                run = Run.objects.create(shift = dummy_shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
                runs.append(run)
        
            return (runs, shift_runs, shift, date_range)

        if case_num == 9:
            shift_start_date = date(2016,4,23)
            shift_end_date = date(2016,4,26)
            shift_start_time = time(00,00)
            shift_end_time = time(23,59)

            shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
            shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)
            shift_info = [shift_start_datetime, shift_end_datetime]
            runs = []
            shift_runs = []

            run_times_list = [
                {'start_time':time(20,00), 'end_time': time(3,00)},
                {'start_time':time(3,00), 'end_time': time(7,00)},
                {'start_time':time(21,00), 'end_time': time(2,00)},  
            ]
            
            shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
            dummy_shift = Shift.objects.create(start_datetime=shift_start_datetime, end_datetime = shift_end_datetime)
            date_range = [shift_start_datetime, shift.end_datetime]
            last_end_date = shift_start_datetime.date()

            for run in shift.runs_related.all():
                shift_runs.append(run)

            for key in run_times_list:
                run_start_datetime = make_aware(datetime.combine(last_end_date, key['start_time']),utc)
                run_end_datetime =  make_aware(datetime.combine(last_end_date, key['end_time']), utc)
                if run_start_datetime > run_end_datetime:
                    run_end_datetime += timedelta(days=1)
               
                last_end_date = run_end_datetime.date()
                run = Run.objects.create(shift = dummy_shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
                runs.append(run)
        
            
            return (runs, shift_runs, shift, date_range)

        if case_num == 10:
            shift_start_date = date(2016,4,18)
            shift_end_date = date(2016,4,18)
            shift_start_time = time(11,00)
            shift_end_time = time(15,00)

            shift_start_datetime = make_aware(datetime.combine(shift_start_date,shift_start_time), utc)
            shift_end_datetime = make_aware(datetime.combine(shift_start_date,shift_end_time),utc)
            total_dur = abs(shift_start_datetime.hour - shift_end_datetime.hour)
            shift_info = [shift_start_datetime, shift_end_datetime]
            runs = []
            run_times_list = [
                {'start_time':time(11,00), 'end_time': time(12,00)}, 
                {'start_time':time(12,00),'end_time':time(13,00)},
                {'start_time':time(13,00), 'end_time':time(14,00)},
                {'start_time':time(14,00), 'end_time':time(15,00)}
            ]
            
            shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
            dummy_shift = Shift.objects.create(start_datetime=shift_start_datetime, end_datetime = shift_end_datetime)
            for key in run_times_list:
                run_start_datetime = make_aware(datetime.combine(shift_start_date, key['start_time']),utc)
                run_end_datetime =  make_aware(datetime.combine(shift_start_date, key['end_time']), utc)
                run = Run.objects.create(shift = dummy_shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
                runs.append(run)
        
            return (shift,runs, total_dur)

        if case_num == 11:
            shift_start_date = date(2016,4,19)
            shift_end_date = date(2016,4,21)
            shift_start_time = time(00,30)
            shift_end_time = time(23,30)
            shift_start_datetime = make_aware(datetime.combine(shift_start_date, shift_start_time), utc)
            shift_end_datetime = make_aware(datetime.combine(shift_end_date,shift_end_time),utc)
            runs = []
            shift_runs = []

            run_times_list = [
                    {'start_time':time(18,30), 'end_time':time(19,30)},
                    {'start_time':time(20,30), 'end_time':time(21,30)},
                    {'start_time':time(21,30), 'end_time':time(22,30)},
                    {'start_time':time(23,30), 'end_time':time(0,30)}, 
                    {'start_time':time(00,30), 'end_time':time(1,30)},
                    {'start_time':time(1,30), 'end_time':time(2,30)},
                    {'start_time':time(2,30), 'end_time':time(3,30)},
                    {'start_time':time(3,30), 'end_time':time(4,30)},
            ]
            
            shift = Shift.objects.create_shift(shift_start_datetime, shift_end_datetime, run_times_list)
            dummy_shift = Shift.objects.create(start_datetime = shift_start_datetime, end_datetime = shift_end_datetime)
            
            for run in shift.runs_related.all():
                shift_runs.append(run)

            for key in run_times_list:
                run_start_datetime = make_aware(datetime.combine(shift_start_date,key['start_time']),utc)
                run_end_datetime =  make_aware(datetime.combine(shift_start_date, key['end_time']), utc)
                run = Run.objects.create(shift = dummy_shift, start_datetime = run_start_datetime, end_datetime = run_end_datetime)
                runs.append(run)

            return (runs, shift_runs, shift)

    def same_run(self, run, shift_run):
        same = False
        if shift_run.start_datetime == run.start_datetime:
            if shift_run.end_datetime == run.end_datetime:
                same = True
        return same

    def run_overlap(self, runs, shift_runs, shift, date_range):
        overlap = False
        num_correct_runs = 0
        #check that the number of runs in runs is equal to the number of runs in shift
        if len(runs) != shift.runs_related.count():
            overlap = True
        #check that the consecutive runs in shift don't overlap
        else:
            for i in range(0,shift.runs_related.count() + 1):
                if i < len(shift_runs) - 1:
                    current_run = shift_runs[i]
                    next_run = shift_runs[i + 1]
                    if current_run.end_datetime > next_run.start_datetime:
                        overlap = True
                        break
                    if current_run.start_datetime < date_range[0] or current_run.end_datetime > date_range[1]:
                        if next_run.start_datetime < date_range[0] or next_run.end_datetime < date_range[1]:
                            overlap = True
                            break

            for run in runs:
                for shift_run in shift.runs_related.all():
                    same = self.same_run(run, shift_run)
                    if same:
                        num_correct_runs = num_correct_runs + 1

            if num_correct_runs == len(runs):
                overlap = False
            else:
                overlap = True

        return overlap

    def test_shift_creation_start_datetime(self):
      case_num = 1
      (shift, shift_info, run) = self.set_up(case_num)
      self.assertEqual(shift.start_datetime, shift_info[0])

    def test_shift_creation_end_datetime(self):
      case_num = 1
      (shift, shift_info, run) = self.set_up(case_num)
      self.assertEqual(shift.end_datetime, shift_info[1])
    
    def test_single_day_one_run(self):
      case_num = 1
      (shift, shift_info, run) = self.set_up(case_num)
      shift_run = shift.runs_related.first()
      same = self.same_run(run, shift_run)
      self.assertTrue(same)

    def test_single_day_two_runs(self):
      case_num = 2
      (runs, shift_runs, shift, date_range) = self.set_up(case_num)
      overlap = self.run_overlap(runs, shift_runs, shift, date_range)
      self.assertFalse(overlap)

    def test_single_day_three_runs(self):
      case_num = 3
      (runs, shift_runs, shift, date_range) = self.set_up(case_num)
      overlap = self.run_overlap(runs, shift_runs, shift, date_range)
      self.assertFalse(overlap)

    def test_two_day_one_run(self):
      case_num = 4
      (runs, shift_runs, shift, date_range) = self.set_up(case_num)
      overlap = self.run_overlap(runs, shift_runs, shift, date_range)
      self.assertFalse(overlap)

    def test_two_day_two_non_midnight(self):
      case_num = 5
    #   (runs, shift_runs, shift, date_range) = self.set_up(case_num)
    #   overlap = self.run_overlap(runs, shift_runs, shift, date_range)
    #   self.assertFalse(overlap)

    def test_two_day_three_middle_midnight(self):
        case_num = 6
        (runs, shift_runs, shift, date_range) = self.set_up(case_num)
        overlap = self.run_overlap(runs, shift_runs, shift, date_range)
        self.assertFalse(overlap)

    def test_three_day_three_non_midnight(self):
        case_num = 7
        (runs, shift_runs, shift, date_range) = self.set_up(case_num)
        overlap = self.run_overlap(runs, shift_runs, shift, date_range)
        self.assertFalse(overlap)

    def test_three_day_two_run_midnight(self):
        case_num = 8
        (runs, shift_runs, shift, date_range) = self.set_up(case_num)
        overlap = self.run_overlap(runs, shift_runs, shift, date_range)
        self.assertFalse(overlap)
        
    def test_three_day_three_run_first_last_midnight(self): 
        case_num = 9
        (runs, shift_runs, shift, date_range) = self.set_up(case_num)
        overlap = self.run_overlap(runs, shift_runs, shift, date_range)
        self.assertFalse(overlap)

    def test_num_shift_runs(self):
      case_num = 10
      (shift, runs, num_expected_runs) = self.set_up(case_num)
      num_shift_runs = shift.runs_related.count()
      self.assertEqual(num_shift_runs, num_expected_runs)

    def test_shift_first_run(self):
      case_num = 10
      (shift, runs, num_expected_runs) = self.set_up(case_num)
      num_shift_runs = shift.runs_related.count()
      shift_first_run = shift.runs_related.first()
      expected_first_run = runs[0]
      self.assertEqual(shift_first_run.start_datetime, expected_first_run.start_datetime)

    def test_shift_last_run(self):
      case_num = 10
      (shift, runs, num_expected_runs) = self.set_up(case_num)
      num_shift_runs = shift.runs_related.count()
      shift_last_run = shift.runs_related.last()
      expected_final_run = runs[len(runs) - 1]
      self.assertEqual(shift_last_run.start_datetime, expected_final_run.start_datetime)

    def test_twenty_four_hour_run(self):
      case_num = 11
      (runs, shift_runs, shift) = self.set_up(case_num)
      twenty_four_confirmed = False
      before_midnight_datetime = make_aware(datetime.combine(date(2016,4,19),time(23,30)),utc)
      the_run = runs[3]
      the_shift_run = shift.runs_related.get(start_datetime=before_midnight_datetime) # won't work if multiple runs have this start time

      if the_shift_run.start_datetime < the_shift_run.end_datetime:
          twenty_four_confirmed = True
        
      self.assertTrue(twenty_four_confirmed)
