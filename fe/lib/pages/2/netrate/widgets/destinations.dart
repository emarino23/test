import 'package:flutter/material.dart';
import 'package:naver_crs/index.dart';
import 'customformdestination.dart';

// ignore: must_be_immutable
class Destinations extends StatelessWidget {
  const Destinations({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    List<Widget> dests = [];
    var tour = globalctx.memory["tour"];
    var destinations = tour["destinations"];
    try {
      if (destinations.isNotEmpty) {
        var i = 0;
        globalctx.memory["totals"]["destSize"] ??= destinations.length;
        for (var dest in destinations) {
          // var destData = getDestinationById(dest);
          var key = GlobalKey();
          globalctx.keys["destination-$i"] = key;
          dests.add(CustomFormDestination(index: i, destination: dest));
          i++;
        }
      }
    } catch (e) {
      log(e);
    }

    return Column(
      children: dests,
    );
  }
}
