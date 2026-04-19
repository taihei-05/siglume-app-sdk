from __future__ import annotations

import click

from siglume_api_sdk.cli.project import render_json, score_project


@click.command("score")
@click.option("--remote", "mode", flag_value="remote", default=True, help="Use the platform preview scorer.")
@click.option("--offline", "mode", flag_value="offline", help="Reserved for v0.4 (PR-C2).")
@click.option("--json", "json_output", is_flag=True, help="Emit machine-readable JSON.")
@click.argument("path", required=False, default=".")
def score_command(mode: str, json_output: bool, path: str) -> None:
    report = score_project(path, mode=mode)
    if json_output:
        click.echo(render_json(report))
    else:
        quality = report["quality"]
        click.secho("Score passed." if report["ok"] else "Score failed.", fg="green" if report["ok"] else "red")
        click.echo(f"Remote quality: {quality['grade']} ({quality['overall_score']}/100)")
    if not report["ok"]:
        raise SystemExit(1)
