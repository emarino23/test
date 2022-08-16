import 'package:flutter/material.dart';

import '../../index.dart';

TimeOfDay minutesToTimeOfDay(int minutes) {
  Duration duration = Duration(minutes: minutes);
  List<String> parts = duration.toString().split(':');
  return TimeOfDay(hour: parseInt(parts[0]), minute: parseInt(parts[1]));
}

extension TimeOfDayExtension on TimeOfDay {
  TimeOfDay addHour(int hour) {
    return replacing(hour: this.hour + hour, minute: minute);
  }

  TimeOfDay addMinute(int min) {
    TimeOfDay newTimeofDay = minutesToTimeOfDay(hour * 60 + minute + min);
    return newTimeofDay;
  }

  TimeOfDay subMinute(int min) {
    TimeOfDay newTimeofDay = minutesToTimeOfDay(hour * 60 + minute - min);
    return newTimeofDay;
  }
}
