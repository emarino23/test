import 'package:flutter/material.dart';
import 'package:get/get.dart';
import '../../index.dart';
import 'package:naver_crs/index.dart';

class DragableExperience extends StatelessWidget {
  const DragableExperience({
    Key? key,
    required this.experience,
    required this.suggested,
  }) : super(key: key);

  final experience;
  final bool suggested;
  @override
  Widget build(BuildContext context) {
    var experienceOptionWidget = ExperienceOptionWidget(
      experience: experience.description,
      suggested: suggested,
      height: Get.height * 0.08,
      width: Get.width * 0.2,
    );

    String title = experience.description;

    return Draggable<String>(
      maxSimultaneousDrags: expDraggable.value,
      data: title,
      feedback: experienceOptionWidget,
      childWhenDragging: experienceOptionWidget,
      child: experienceOptionWidget,
    );
  }
}
