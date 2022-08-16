import 'package:flutter/material.dart';
import 'package:naver_crs/index.dart';
import 'customdescription.dart';

class Cover extends StatelessWidget {
  const Cover({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Map tour = globalctx.memory["tour"];
    var customer = tour["tour"]["lead_passenger"];
    var pax = tour["tour"]["passengers"];
    var days = tour["days"];
    return Center(
      child: Column(
        children: [
          CustomDescriptionWidget(
              textAlign: TextAlign.center,
              text: "Net Rate: ${tour["description"]}",
              width: 0.5,
              fontSize: 18,
              fontWeight: FontWeight.bold),
          CustomDescriptionWidget(
              textAlign: TextAlign.center,
              text: "$customer ${days}D/${days - 1}N x $pax",
              width: 0.2,
              fontSize: 18,
              fontWeight: FontWeight.bold),
        ],
      ),
    );
  }
}
