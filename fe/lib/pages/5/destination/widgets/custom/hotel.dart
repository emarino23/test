import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../../../../../index.dart';

class HotelWidget extends StatelessWidget {
  const HotelWidget({
    Key? key,
    required this.index,
  }) : super(key: key);

  final index;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        const CustomTitleWidget(
            width: 0.225,
            fontWeight: FontWeight.bold,
            label: "  Hotel Information  "),
        Obx(() => RoundedFormButton(
              color: Colors.grey,
              label: hotelName.value,
              height: 0.05,
              fontSize: 12,
              fontWeight: FontWeight.bold,
              textColor: Colors.black,
              onPressed: () async {
                showHotelResultDialog(context, id: 0, index: index);
              },
            ))
      ],
    );
  }
}
