# New content of record.py with the updated embed field

embed.add_field(
    name=f"{EMOJIS['general']} __**Recording Settings**__",
    value=f"```Auto-Stop Limit (boost-based): {self.get_autostop_limit(ctx.guild)//60} minute(s)\nUpload Limit: {self.format_file_size(upload_limit)}```",
    inline=False
)