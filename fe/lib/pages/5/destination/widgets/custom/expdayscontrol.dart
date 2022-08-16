import 'package:flutter/material.dart';

import '../../../../../index.dart';

class ExpDaysCounterWidget extends StatelessWidget {
  const ExpDaysCounterWidget({
    Key? key,
    required this.index,
    required this.type,
  }) : super(key: key);

  final index;
  final type;

  @override
  Widget build(BuildContext context) {
    return CustomFormCounterFieldWidget(
        initial: parseInt(getFormValue(
            globalctx.memory["destinations"], index, "explorationDay", "0")),
        min: 0,
        max: checkMaxDaysValue(type),
        bound: 0,
        onValueChanged: (value) {
          setFormValue(
              globalctx.memory["destinations"], index, "explorationDay", value);
          updateTotalLeftAccumulated();
        },
        label: "  Exploration Days     ",
        width: 0.20);
  }
}
